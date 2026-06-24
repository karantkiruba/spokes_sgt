import frappe

@frappe.whitelist(allow_guest=True)
def get_portal_count():

    count = frappe.db.get_value(
        "Spokes E-Invoice Portal",
        {},
        "count",
        order_by="modified desc"
    )

    return {
        "site": frappe.local.site,
        "count": count or 0
    }
