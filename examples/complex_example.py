def generate_monthly_report(users, transactions, tax_rate, discount, region, include_summary):
    report = {}
    total_revenue = 0
    active_users = 0

    for user in users:
        user_total = 0

        if user["active"]:
            active_users += 1

            for tx in transactions:
                if tx["user_id"] == user["id"]:
                    amount = tx["amount"]

                    if region == "international":
                        amount += amount * tax_rate

                    if discount > 0:
                        amount -= discount

                    user_total += amount

        report[user["name"]] = user_total
        total_revenue += user_total

    if include_summary:
        report["summary"] = {
            "total_users": len(users),
            "active_users": active_users,
            "total_revenue": total_revenue
        }

    return report
