class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        # Processamento dos dados com base nas entradas
        processed_data = {
            'total_employees': int(self.data['num_funcionarios']),
            'total_revenue': float(self.data['faturamento']),
            'business_type': self.data['segmento']
        }
        return processed_data
