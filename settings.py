import os

# =================================
#   DOBIE SETTINGS
# =================================
DOBIE_HOST = os.environ.get('DOBIE_HOST', 'localhost')
DOBIE_PORT = os.environ.get('DOBIE_PORT', 9006)

# =================================
#   FUSEKI SERVER SETTINGS
# =================================
FUSEKI_SERVER_HOST = os.environ.get('FUSEKI_SERVER_HOST', 'localhost')
FUSEKI_SERVER_PORT = os.environ.get('FUSEKI_SERVER_PORT', 3030)
FUSEKI_SERVER_DATASET = os.environ.get('FUSEKI_SERVER_DATASET', 'saro')

# =================================
#   RABBITMQ SETTINGS
# =================================
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT', 5672)
RABBITMQ_VHOST = os.environ.get('RABBITMQ_VHOST', '/')
RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'rabbitmq')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'rabbitmq')

# =================================
#   POSTGRES SETTINGS
# =================================

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'admin')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'admin')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'api_db')

ENGINE_STRING = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB
)

JOB_POSTS_TABLE = 'job_post'

# =================================
#   APPLICATION SETTINGS
# =================================
APP_QUEUE = os.environ.get('APP_QUEUE', "mediator_queue")

SARO_SKILL = """saro:{meta_value} a saro:{Kind} ;
	 saro:icCoreTo saro:ICT ;
	 rdfs:label "{String}" .
	 
	 """

SARO_PREFIXES = """
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix saro: <http://w3id.org/saro#> .
@prefix esco: <http://data.europa.eu/esco/model#> .

"""

STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

BATCH_SIZE = 50
TIME_BETWEEN_REQUESTS = 10  # in seconds

JOB_NAMES = {
    "backend_developer": {'queries': ['backend developer', 'backend engineer'], 'min_score': 3},
    "frontend_developer": {'queries': ['frontend developer', 'frontend engineer'], 'min_score': 3},
    "database_developer": {'queries': ['database developer', 'database engineer'], 'min_score': 3},
    "hardware_engineer": {'queries': ['hardware', 'hardware engineer'], 'min_score': 3},
    "data_analyst": {'queries': ['data analyst', 'data scientist'], 'min_score': 3},
    "data_engineer": {'queries': ['data engineer', 'big data'], 'min_score': 4},
    "machine_learning_engineer": {'queries': ['machine learning engineer', 'machine learning'], 'min_score': 4},
    "network_architect": {'queries': ['network engineer', 'network architect'], 'min_score': 4},
    "dev_ops_engineer": {'queries': ['DevOps engineer'], 'min_score': 4},
    "security_engineer": {'queries': ['security engineer', 'security'], 'min_score': 3},
    "web_developer": {'queries': ['web engineer', 'web developer'], 'min_score': 4},
    "mobile_developer": {'queries': ['android developer', 'ios developer'], 'min_score': 4},
    "qa_engineer": {'queries': ['quality assurance', 'qa engineer'], 'min_score': 4},
    "business_analyst": {'queries': ['business analyst', 'business development', 'business intelligence'],
                         'min_score': 4},
    "ui_ux_designer": {'queries': ['ui/ux', 'ux/ui'], 'min_score': 7},
    "project_manager": {'queries': ['project manager', 'technical manager'], 'min_score': 4},
    "test_developer": {'queries': ['test developer', 'test engineer', 'software engineer in test'], 'min_score': 4}
}

# AnalEyeZer Settings
ANALEYEZER_HOST = os.environ.get('ANALEYEZER_HOST', 'localhost')
ANALEYEZER_PORT = os.environ.get('ANALEYEZER_PORT', 5002)
INDEX = "job_post_index"
QUERY_EXECUTOR_URL = 'http://{}:{}/ask/storage'.format(ANALEYEZER_HOST, ANALEYEZER_PORT)

# Extraction Pipeline Settings
SAVE_IN_FILE = False

# =================================
#   CELERY SETTINGS
# =================================
CELERY_BROKER_URL = 'pyamqp://{}:{}@{}:{}/{}'.format(
    RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST)

CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_ACKS_LATE = True
