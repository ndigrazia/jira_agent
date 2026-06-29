#!/bin/bash

source setup_gcp.sh

#echo "Authenticating with Google Cloud..."
#gcloud auth login
#gcloud config set project $GOOGLE_CLOUD_PROJECT

#echo "Setting up virtual environment..."
#source .venv/bin/activate
#uv sync

#adk web . 

echo ""
echo "Verifying gcloud configuration..."
gcloud config list --format='text(core.project, compute.region)'

echo "GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT"
echo "GOOGLE_CLOUD_LOCATION=$GOOGLE_CLOUD_LOCATION"

adk deploy cloud_run \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --service_name=jira-agent-service \
  --with_ui \
  ../jira_agent