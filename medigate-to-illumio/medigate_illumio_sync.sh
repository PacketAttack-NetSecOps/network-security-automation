set -euo pipefail

# Medigate
export MEDIGATE_BASE_URL="https://api.medigate.io"
export MEDIGATE_API_TOKEN="ADD TOKEN"

# Illumio
export ILLUMIO_PCE_HOST="https://us-scp41.illum.io"
export ILLUMIO_ORG_ID="4325424"
export ILLUMIO_API_KEY_ID="ADD API KEY ID"
export ILLUMIO_API_KEY_SECRET="ADD SECRET"
export AUTO_PROVISION=true

# Job-specific
export TARGET_IPLIST_NAME="MEDIGATE-Medical-Critical"
export LOG_LEVEL="INFO"

cd /home/packetattack/automation_smg/medigate_illumio
/usr/bin/python3 MEDIGATE-Medical-Critical_sync-provision.py >> /home/packetattack/automation_smg/medigate_illumio/logs/MEDIGATE-Medical-Critical_sync-provision.log 2>&1
