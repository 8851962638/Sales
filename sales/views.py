# sales/views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from django.contrib import messages
from openpyxl import Workbook
from .models import Product
import json


from .forms import CostUploadForm, ReferralFeeUploadForm


# View for uploading referral fee file
def upload_referral_fee(request):
    if request.method == 'POST' and request.FILES['referral_fee_file']:
        # Process the uploaded file
        referral_fee_file = request.FILES['referral_fee_file']
        
        # Read the file into a pandas DataFrame (assuming it's an Excel file)
        try:
            df = pd.read_excel(referral_fee_file)
            # Example: Ensure the columns are correct
            if 'Product Name' not in df.columns or 'Referral Fee' not in df.columns:
                messages.error(request, "Invalid file format.")
                return redirect('upload_referral_fee')
            
            # Save the file data in session or database for further processing
            request.session['referral_fee_data'] = df.to_dict(orient='records')
            messages.success(request, "File uploaded successfully!")
            return redirect('upload_cost')  # Redirect to the next step (upload cost page)
        except Exception as e:
            messages.error(request, f"Error processing file: {str(e)}")
            return redirect('upload_referral_fee')

    # GET request: Display the file upload form
    form = ReferralFeeUploadForm()
    return render(request, 'sales/upload_referral_fee.html', {'form': form})

# View for uploading cost file and processing the data
# sales/views.py
# View for uploading cost file and processing the data
def upload_cost(request):
    if request.method == 'POST' and request.FILES['cost_file']:
        cost_file = request.FILES['cost_file']
        
        # Read the cost file into a pandas DataFrame
        try:
            cost_df = pd.read_excel(cost_file)
            if 'Product Name' not in cost_df.columns or 'Cost' not in cost_df.columns:
                messages.error(request, "Invalid file format.")
                return redirect('upload_cost')
            
            referral_fee_data = request.session.get('referral_fee_data')
            if not referral_fee_data:
                messages.error(request, "Referral fee data is missing.")
                return redirect('upload_referral_fee')

            referral_fee_df = pd.DataFrame(referral_fee_data)
            merged_df = pd.merge(referral_fee_df, cost_df, on='Product Name')
            merged_df['Total Cost'] = merged_df['Cost'] * merged_df['Referral Fee']

            # Save to the database
            Product.objects.all().delete()  # Clear old data
            for _, row in merged_df.iterrows():
                Product.objects.create(
                    name=row['Product Name'],
                    cost=row['Cost'],
                    referral_fee=row['Referral Fee'],
                    total_cost=row['Total Cost']
                )

            # Save to an Excel file for download
            output_file = 'processed_sales_data.xlsx'
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={output_file}'
            merged_df.to_excel(response, index=False)
            return response
        except Exception as e:
            messages.error(request, f"Error processing file: {str(e)}")
            return redirect('upload_cost')

    form = CostUploadForm()
    return render(request, 'sales/upload_cost.html', {'form': form})



# View for displaying total sales and product-specific data
def user_data(request):
    # Fetch all product data
    products = Product.objects.all()

    # Calculate total sales
    total_sales = sum([product.total_cost for product in products])

    # Prepare data for JSON
    product_data = list(products.values('name', 'total_cost'))

    context = {
        'total_sales': total_sales,
        'products': products,  # Pass products for the buttons
        'product_data': json.dumps(product_data),  # Serialize to JSON
    }

    return render(request, 'sales/user_data.html', context)