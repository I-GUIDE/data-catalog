# Catalog Submission Template

### Keycloak
keycloak is used with the oidc protocol for user authentication.  This template uses the CUAHSI keycloak image.  It is currently being developed so for now you must clone the repo and build the image to use it here.  At a later time we will be pushing tagged images to an artifact repository that can simply be pulled.
- `git clone git@github.com:CUAHSI/keycloak.git`
- `cd keycloak`
- `mvn clean install`
- `docker build -t cuahsi/cuahsi-keycloak:latest .`

### postgresdb
Used exclusiviely by keycloak

### nginx
nginx is used for routing between all the services and handle ssl certificates.  Because some identity providers who use the oidc protocol requires ssl, a default certificate is included with this project.  Of course, these certificates should only be used for local development.
- `https://localhost`

### api
The api service is a base python image with some dependencies installed for development with FastAPI.

### mongodb
The database configured for use in FastAPI with Beanie