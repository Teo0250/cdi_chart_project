from cdi_rate_extraction import cdi_extraction
from cdi_rate_chart import generate_chart

if __name__ == "__main__":
    cdi_extraction()
    name_chart = 'cdi_chart.png'
    generate_chart(name_chart)