import os
from django.core.exceptions import ValidationError

def validate_pdf(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext != '.pdf':
        raise ValidationError("Somente arquivos PDF são permitidos.")

def validate_file_size(file):
    max_size_mb = 5
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"O arquivo não pode exceder {max_size_mb} MB.")
