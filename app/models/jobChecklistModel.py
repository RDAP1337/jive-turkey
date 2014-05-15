from app import db


class JobChecklist(db.Model):
    __tablename__ = 'job_checklist'

    id = db.Column(db.Integer, primary_key=True)
    job_checklist_has_signed_contract = db.Column(db.Boolean)
    job_checklist_has_color_selection_sheet = db.Column(db.Boolean)
    job_checklist_has_precautionary_letter = db.Column(db.Boolean)
    job_checklist_has_roof_siding_specs = db.Column(db.Boolean)
    job_checklist_has_pre_job_photos = db.Column(db.Boolean)
    job_checklist_has_p_and_l = db.Column(db.Boolean)
    job_checklist_has_permit = db.Column(db.Boolean)
    job_checklist_has_connect_point = db.Column(db.Boolean)
    job_checklist_has_work_order = db.Column(db.Boolean)
    job_checklist_has_company_estimate = db.Column(db.Boolean)
    job_checklist_has_company_warranty = db.Column(db.Boolean)
    job_checklist_has_manufacturer_warranty = db.Column(db.Boolean)
    job_checklist_has_first_check_acv = db.Column(db.Boolean)
    job_checklist_has_depreciation_check = db.Column(db.Boolean)
    job_checklist_has_coupon = db.Column(db.Boolean)
    job_checklist_has_rai_invoice = db.Column(db.Boolean)
    job_checklist_has_final_invoice = db.Column(db.Boolean)
    job_checklist_has_receipt = db.Column(db.Boolean)
    job_checklist_has_insurance_estimate = db.Column(db.Boolean)

    def __init__(
            self,
            job_checklist_has_signed_contract,
            job_checklist_has_color_selection_sheet,
            job_checklist_has_precautionary_letter,
            job_checklist_has_roof_siding_specs,
            job_checklist_has_pre_job_photos,
            job_checklist_has_p_and_l,
            job_checklist_has_permit,
            job_checklist_has_connect_point,
            job_checklist_has_work_order,
            job_checklist_has_company_estimate,
            job_checklist_has_company_warranty,
            job_checklist_has_manufacturer_warranty,
            job_checklist_has_first_check_acv,
            job_checklist_has_depreciation_check,
            job_checklist_has_coupon,
            job_checklist_has_rai_invoice,
            job_checklist_has_final_invoice,
            job_checklist_has_receipt,
            job_checklist_has_insurance_estimate
    ):
        self.job_checklist_has_signed_contract = job_checklist_has_signed_contract
        self.job_checklist_has_color_selection_sheet = job_checklist_has_color_selection_sheet
        self.job_checklist_has_precautionary_letter = job_checklist_has_precautionary_letter
        self.job_checklist_has_roof_siding_specs = job_checklist_has_roof_siding_specs
        self.job_checklist_has_pre_job_photos = job_checklist_has_pre_job_photos
        self.job_checklist_has_p_and_l = job_checklist_has_p_and_l
        self.job_checklist_has_permit = job_checklist_has_permit
        self.job_checklist_has_connect_point = job_checklist_has_connect_point
        self.job_checklist_has_work_order = job_checklist_has_work_order
        self.job_checklist_has_company_estimate = job_checklist_has_company_estimate
        self.job_checklist_has_company_warranty = job_checklist_has_company_warranty
        self.job_checklist_has_manufacturer_warranty = job_checklist_has_manufacturer_warranty
        self.job_checklist_has_first_check_acv = job_checklist_has_first_check_acv
        self.job_checklist_has_depreciation_check = job_checklist_has_depreciation_check
        self.job_checklist_has_coupon = job_checklist_has_coupon
        self.job_checklist_has_rai_invoice = job_checklist_has_rai_invoice
        self.job_checklist_has_final_invoice = job_checklist_has_final_invoice
        self.job_checklist_has_receipt = job_checklist_has_receipt
        self.job_checklist_has_insurance_estimate = job_checklist_has_insurance_estimate