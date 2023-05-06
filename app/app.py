from flask_restful import Api
from app.clients.urls import ClientsUrls, ClientsSearchUrls, ClientUrls
from app.pets.urls import PetsUrls, PetsSearchUrls, PetUrls
from . import create_app # from __init__ file


app = create_app()

api = Api(app)
api.add_resource(ClientsUrls, '/clients')
api.add_resource(ClientsSearchUrls, '/clients/search/<search_clients>')
api.add_resource(ClientUrls, '/client/<int:pk>')
api.add_resource(PetsUrls, '/pets')
api.add_resource(PetsSearchUrls, '/pets/search/<search_pets>')
api.add_resource(PetUrls, '/pet/<int:pk>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')