from odoo import fields, models, api

class SaleOrderCustomReportLine(models.Model):
    _name = 'sale.order.custom.report.line'
    _description = 'Báo cáo chi tiết đơn hàng'
    _auto = False

    id = fields.Integer(string='ID', readonly=True)
    order_id = fields.Many2one('sale.order', string='Đơn hàng', readonly=True)
    name = fields.Char(string='Mã đơn hàng', readonly=True)  
    order_date = fields.Date(string='Ngày đặt hàng', readonly=True)
    customer_id = fields.Many2one('res.partner', string='Khách hàng', readonly=True)
    city = fields.Char(string='Thành phố', readonly=True)
    user_id = fields.Many2one('res.users', string='Nhân viên bán hàng', readonly=True)
    product_id = fields.Many2one('product.product', string='Sản phẩm', readonly=True)
    product_category_id = fields.Many2one('product.category', string='Loại sản phẩm', readonly=True)
    product_uom_qty = fields.Float(string='Số lượng', readonly=True)
    price_unit = fields.Float(string='Đơn giá', readonly=True)
    price_subtotal = fields.Float(string='Thành tiền', readonly=True)
    line_price_total = fields.Float(string='Tổng tiền dòng', readonly=True)
    order_price_total = fields.Float(string='Tổng tiền đơn hàng', readonly=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('sent', 'Đã gửi'),
        ('sale', 'Xác nhận'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy'),
    ], string='Trạng thái đơn', readonly=True)
    invoice_status = fields.Selection([
        ('upselling', 'Upselling Opportunity'),
        ('invoiced', 'Fully Invoiced'),
        ('to invoice', 'To Invoice'),
        ('no', 'Nothing to Invoice')
    ], string='Trạng thái hóa đơn', readonly=True)
    payment_term_id = fields.Many2one('account.payment.term', string='Điều khoản thanh toán', readonly=True)
    company_id = fields.Many2one('res.company', string='Công ty', readonly=True)
    currency_id = fields.Many2one('res.currency', string='Tiền tệ', readonly=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Bảng giá', readonly=True)
    warehouse_id = fields.Many2one('stock.warehouse', string='Kho hàng', readonly=True)
    team_id = fields.Many2one('crm.team', string='Đội ngũ bán hàng', readonly=True)

    def init(self):
        tools = self.env['ir.module.module']
        self.env.cr.execute("""
            DROP VIEW IF EXISTS sale_order_custom_report_line;
            CREATE OR REPLACE VIEW sale_order_custom_report_line AS (
                SELECT
                    sol.id AS id,
                    so.id AS order_id,
                    so.name AS name,
                    so.date_order::date AS order_date,
                    so.partner_id AS customer_id,
                    rp.city AS city,
                    so.user_id AS user_id,
                    sol.product_id AS product_id,
                    pt.categ_id AS product_category_id,
                    sol.product_uom_qty AS product_uom_qty,
                    sol.price_unit AS price_unit,
                    sol.price_subtotal AS price_subtotal,
                    sol.price_total AS line_price_total,
                    so.amount_total AS order_price_total,
                    so.state AS state,
                    so.invoice_status AS invoice_status,
                    so.payment_term_id AS payment_term_id,
                    so.company_id AS company_id,
                    so.currency_id AS currency_id,
                    so.pricelist_id AS pricelist_id,
                    so.warehouse_id AS warehouse_id,
                    so.team_id AS team_id
                FROM sale_order_line sol
                JOIN sale_order so ON sol.order_id = so.id
                LEFT JOIN res_partner rp ON so.partner_id = rp.id
                LEFT JOIN product_product pp ON sol.product_id = pp.id
                LEFT JOIN product_template pt ON pp.product_tmpl_id = pt.id
            )
        """)
