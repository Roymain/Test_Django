sleep 45
# echo done
# python manage.py migrate
# python manage.py collectstatic --noinput

# python manage.py runserver 0.0.0.0:8000


set -e

# Fonction pour vérifier si la base de données est prête
check_db() {
  echo "Vérification de la disponibilité de la base de données..."
  while ! mysqladmin ping -h"db" -P"3001" -u"admin" -p"passwordadmin" --silent; do
    echo "La base de données n'est pas encore prête. Attente..."
    sleep 10
  done
  echo "La base de données est prête."
}

# Appel de la fonction de vérification de la base de données
check_db

# Exécution des commandes de migration et de collecte des fichiers statiques
echo "Exécution des migrations de la base de données..."
python manage.py migrate

echo "Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

# Démarrage du serveur backend
echo "Démarrage du serveur backend..."
python manage.py runserver 0.0.0.0:8000