import yaml

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Cosine Similarity Function
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))