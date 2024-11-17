# sales/forms.py
from django import forms

class ReferralFeeUploadForm(forms.Form):
    referral_fee_file = forms.FileField(label='Upload Referral Fee File')

# sales/forms.py
class CostUploadForm(forms.Form):
    cost_file = forms.FileField(label='Upload Cost File')

