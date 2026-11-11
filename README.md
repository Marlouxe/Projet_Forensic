<img src="./front/public/img/logo.png" alt="logo" width="200"/>

HackBNB est une plateforme en ligne permettant à des professionnels de la cybersécurité de trouver des lieux de séjour adaptés à leurs activités, dans un cadre légal et communautaire.

Pour démarrer le projet en local, utiliser :
```bash
docker compose up
```

puis accéder à la plateforme : http://localhost:9001


## Correctifs de sécurité

Suite à l'audit forensic réalisé par l'équipe CERTAIN, huit vulnérabilités ont été identifiées sur ce dépôt. Le code présent sur la branche `main` correspond à l'état vulnérable analysé lors de l'audit.

**Les correctifs sont disponibles sur la branche `corrigé`.**

Pour récupérer la version corrigée :
```bash
git checkout corrigée
docker compose up
```


Le détail de chaque vulnérabilité et de son correctif est disponible dans le rapport d'audit de l'équipe CERTAIN.
