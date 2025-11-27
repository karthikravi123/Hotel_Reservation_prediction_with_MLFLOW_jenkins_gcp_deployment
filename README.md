Hotel Reservation Prediciton


##setup jenkins Cntainer

docker run -d --name jenkins-dind --privileged -p 8080:8080 -p 50000:50000 -v //var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins-dind


##run and copy password to start jenkins
docker logs jenkins-dind

##browser - localhost:8080


===============================================================================

##install dependencies on jenkins container
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
apt install -y python3-venv
exit

===============================================================================

STEP 1 — Create keyrings directory
mkdir -p /etc/apt/keyrings

✅ STEP 2 — Download Google Cloud public key
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    -o /etc/apt/keyrings/cloud.google.gpg


If you get errors, try:

curl -L https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    -o /etc/apt/keyrings/cloud.google.gpg

✅ STEP 3 — Set correct permissions
chmod 644 /etc/apt/keyrings/cloud.google.gpg

✅ STEP 4 — Add Google Cloud repo (Debian 12)

Use this one (correct format for newer Debian):

echo "deb [signed-by=/etc/apt/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
    | tee /etc/apt/sources.list.d/google-cloud-sdk.list

✅ STEP 5 — Update & Install gcloud
apt update -y
apt install -y google-cloud-sdk

✅ STEP 6 — Verify
gcloud --version


===============================================================================

##grant docker permission to jenkins
groupadd docker
usermod -aG docker jenkins
usermod -aG root jenkins
exit



===============================================================================


Manage jenkins - credentials -system0 global credentials - add credentials
kind- secret file
file upload - service key json file
id - gcp key(any)

giving access to jenkins GCP cloud