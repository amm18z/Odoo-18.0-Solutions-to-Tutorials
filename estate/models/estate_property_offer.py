from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offers for properties, buildings, and collections of buildings, and the land associated with each."

    price = fields.Float(string="Price")
    status = fields.Selection(string="State",copy=False,selection=[('accepted','Accepted'),('refused','Refused')])
    partner_id = fields.Many2one("res.partner", string="Buyer",required=True)
    property_id = fields.Many2one("estate.property",string="Property",required=True)

    validity = fields.Integer(compute='_inverse_date_deadline', inverse='_compute_date_deadline', string='Validity', default='7', store=True)


    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', string="Deadline", store=True, default=fields.Date.add(fields.Date.today(),days=7))

    @api.depends('create_date', 'date_deadline', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date != False:
                record.date_deadline = fields.Date.add(fields.Date.to_date(record.create_date),days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Date.today(), days=record.validity)
            
    @api.depends('create_date', 'validity', 'date_deadline')
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date != False:
                record.validity = (record.date_deadline - fields.Date.to_date(record.create_date)).days
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days