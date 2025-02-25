


SECRET_KEY = '4125b10bfcccc20b35dab6b89ddef452a526dc25ea07decf738070dac2eb817eee6280a10b39def59e841feb310993f9232a2dde50bea85629b19e4c1e937632'
            

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user',  # Ensure this matches your MySQL database name
        'USER': 'sample',  # Ensure this user exists in MySQL
        'PASSWORD': '1234',  # Change this to your actual MySQL password
        'HOST': 'localhost',  # Use 'db' if running in Docker
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',  # Ensures proper Unicode support
        },
    }
}