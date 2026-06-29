
source setup_gcp.sh

gcloud run services delete jira-agent-service \
  --region=$GOOGLE_CLOUD_LOCATION \
  --quiet

gcloud artifacts docker images list \
  $GOOGLE_CLOUD_LOCATION-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/cloud-run-source-deploy \
  --format="value(IMAGE)" | while read image; do
    gcloud artifacts docker images delete "$image" --quiet --delete-tags 2>/dev/null
done

 gcloud artifacts repositories delete cloud-run-source-deploy \
   --location=$GOOGLE_CLOUD_LOCATION \
   --quiet

# Verify cleanup
gcloud run services list --region=$GOOGLE_CLOUD_LOCATION