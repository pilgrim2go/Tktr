def includeme(config):
    config.include('ticketing.boxoffice.methods', route_prefix="/pay")
    config.add_route("buy_tickets", "/buy")
    config.add_route("addons", "/addons")
    config.add_route("order_details", "/details")
    config.add_route("pay_for_tickets", "/pay")
    config.add_route("pay_confirm", "/confirm")
    config.add_route("return_tickets", "/return/{tick_id}")
    config.add_route("alter_payment", "/payment/{tick_id}")
    config.add_route("alter_payment_stripe", "/payment/{payment_id}/stripe")
    config.add_route("alter_payment_cheque", "/payment/{payment_id}/cheque")
    config.add_route("alter_payment_banktransfer", "/payment/{payment_id}/banktransfer")
    config.add_route("alter_confirm", "/payment/{payment_id}/confirm")
