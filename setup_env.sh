#!/bin/sh

echo consumer_key=$consumer_key >> .env
echo consumer_secret=$consumer_secret >> .env
echo access_token=$access_token >> .env
echo access_token_secret=$access_token_secret >> .env

echo WEB_IMAGE=$IMAGE:bot  >> .env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> .env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> .env
echo CI_REGISTRY=$CI_REGISTRY  >> .env
echo IMAGE=$CI_REGISTRY/leptitcoinsante/$CI_PROJECT_NAME >> .env
