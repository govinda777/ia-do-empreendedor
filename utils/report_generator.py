from jinja2 import Environment, FileSystemLoader


def generate_html_report(processed_data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    # Gera o relatório com base nos dados processados
    report_html = template.render(
        total_employees=processed_data["total_employees"],
        total_revenue=processed_data["total_revenue"],
        business_type=processed_data["business_type"],
    )

    return report_html
