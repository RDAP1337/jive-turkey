from app import db


class JobMaterials(db.Model):
    __tablename__ = 'job_materials'

    id = db.Column(db.Integer, primary_key=True)
    job_materials_roof_manufacturer = db.Column(db.String(64))
    job_materials_roof_color = db.Column(db.String(64))
    job_materials_roof_style = db.Column(db.String(64))
    job_materials_siding_manufacturer = db.Column(db.String(64))
    job_materials_siding_color = db.Column(db.String(64))
    job_materials_siding_style = db.Column(db.String(64))
    job_materials_drip_edge_manufacturer = db.Column(db.String(64))
    job_materials_drip_edge_color = db.Column(db.String(64))
    job_materials_drip_edge_style = db.Column(db.String(64))
    job_materials_fascia_manufacturer = db.Column(db.String(64))
    job_materials_fascia_color = db.Column(db.String(64))
    job_materials_fascia_style = db.Column(db.String(64))
    job_materials_gutter_manufacturer = db.Column(db.String(64))
    job_materials_gutter_color = db.Column(db.String(64))
    job_materials_gutter_style = db.Column(db.String(64))
    job_materials_outer_corner_manufacturer = db.Column(db.String(64))
    job_materials_outer_corner_color = db.Column(db.String(64))
    job_materials_outer_corner_style = db.Column(db.String(64))
    job_materials_inner_corner_manufacturer = db.Column(db.String(64))
    job_materials_inner_corner_color = db.Column(db.String(64))
    job_materials_inner_corner_style = db.Column(db.String(64))
    job_materials_window_wrap_manufacturer = db.Column(db.String(64))
    job_materials_window_wrap_color = db.Column(db.String(64))
    job_materials_window_wrap_style = db.Column(db.String(64))
    job_materials_door_wrap_manufacturer = db.Column(db.String(64))
    job_materials_door_wrap_color = db.Column(db.String(64))
    job_materials_door_wrap_style = db.Column(db.String(64))
    job_materials_vents_manufacturer = db.Column(db.String(64))
    job_materials_vents_color = db.Column(db.String(64))
    job_materials_vents_style = db.Column(db.String(64))
    job_materials_valleys_manufacturer = db.Column(db.String(64))
    job_materials_valleys_color = db.Column(db.String(64))
    job_materials_valleys_style = db.Column(db.String(64))

    def __init__(
            self,
            job_materials_roof_manufacturer,
            job_materials_roof_color,
            job_materials_roof_style,
            job_materials_siding_manufacturer,
            job_materials_siding_color,
            job_materials_siding_style,
            job_materials_drip_edge_manufacturer,
            job_materials_drip_edge_color,
            job_materials_drip_edge_style,
            job_materials_fascia_manufacturer,
            job_materials_fascia_color,
            job_materials_fascia_style,
            job_materials_gutter_manufacturer,
            job_materials_gutter_color,
            job_materials_gutter_style,
            job_materials_outer_corner_manufacturer,
            job_materials_outer_corner_color,
            job_materials_outer_corner_style,
            job_materials_inner_corner_manufacturer,
            job_materials_inner_corner_color,
            job_materials_inner_corner_style,
            job_materials_window_wrap_manufacturer,
            job_materials_window_wrap_color,
            job_materials_window_wrap_style,
            job_materials_door_wrap_manufacturer,
            job_materials_door_wrap_color,
            job_materials_door_wrap_style,
            job_materials_vents_manufacturer,
            job_materials_vents_color,
            job_materials_vents_style,
            job_materials_valleys_manufacturer,
            job_materials_valleys_color,
            job_materials_valleys_style
    ):
        self.job_materials_roof_manufacturer = job_materials_roof_manufacturer
        self.job_materials_roof_color = job_materials_roof_color
        self.job_materials_roof_style = job_materials_roof_style
        self.job_materials_siding_manufacturer = job_materials_siding_manufacturer
        self.job_materials_siding_color = job_materials_siding_color
        self.job_materials_siding_style = job_materials_siding_style
        self.job_materials_drip_edge_manufacturer = job_materials_drip_edge_manufacturer
        self.job_materials_drip_edge_color = job_materials_drip_edge_color
        self.job_materials_drip_edge_style = job_materials_drip_edge_style
        self.job_materials_fascia_manufacturer = job_materials_fascia_manufacturer
        self.job_materials_fascia_color = job_materials_fascia_color
        self.job_materials_fascia_style = job_materials_fascia_style
        self.job_materials_gutter_manufacturer = job_materials_gutter_manufacturer
        self.job_materials_gutter_color = job_materials_gutter_color
        self.job_materials_gutter_style = job_materials_gutter_style
        self.job_materials_outer_corner_manufacturer = job_materials_outer_corner_manufacturer
        self.job_materials_outer_corner_color = job_materials_outer_corner_color
        self.job_materials_outer_corner_style = job_materials_outer_corner_style
        self.job_materials_inner_corner_manufacturer = job_materials_inner_corner_manufacturer
        self.job_materials_inner_corner_color = job_materials_inner_corner_color
        self.job_materials_inner_corner_style = job_materials_inner_corner_style
        self.job_materials_window_wrap_manufacturer = job_materials_window_wrap_manufacturer
        self.job_materials_window_wrap_color = job_materials_window_wrap_color
        self.job_materials_window_wrap_style = job_materials_window_wrap_style
        self.job_materials_door_wrap_manufacturer = job_materials_door_wrap_manufacturer
        self.job_materials_door_wrap_color = job_materials_door_wrap_color
        self.job_materials_door_wrap_style = job_materials_door_wrap_style
        self.job_materials_vents_manufacturer = job_materials_vents_manufacturer
        self.job_materials_vents_color = job_materials_vents_color
        self.job_materials_vents_style = job_materials_vents_style
        self.job_materials_valleys_manufacturer = job_materials_valleys_manufacturer
        self.job_materials_valleys_color = job_materials_valleys_color
        self.job_materials_valleys_style = job_materials_valleys_style