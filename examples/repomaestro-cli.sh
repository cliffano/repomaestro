#!/usr/bin/bash
set -o nounset

STAGE_DIR=../stage/examples
mkdir -p ${STAGE_DIR}

printf "\n\n========================================\n"
printf "Show help guide:\n"
repomaestro --help

printf "\n\n========================================\n"
printf "Run command with no arg:\n"
repomaestro

printf "\n\n========================================\n"
printf "Run init command with specified config file and Github ID:"
GITHUB_TOKEN=${STUDIO_GITHUB_TOKEN} repomaestro init --conf-file ${STAGE_DIR}/.repomaestro.yaml --github-ids cliffano

printf "\n\n========================================\n"
printf "Run gen command with specified config file:"
repomaestro gen --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/repoman.j2 --out-file ${STAGE_DIR}/repoman.json
repomaestro gen --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/vscode.j2 --out-file ${STAGE_DIR}/vscode.json

printf "\n\n========================================\n"
printf "Run gen command with specified config file and include exclude keywords:"
repomaestro gen --include-keywords ansible --exclude-keywords openapi --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/repoman.j2 --out-file ${STAGE_DIR}/repoman-filtered.json
repomaestro gen --include-keywords ansible --exclude-keywords openapi --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/vscode.j2 --out-file ${STAGE_DIR}/vscode-filtered.json

printf "\n\n========================================\n"
printf "Run gen command with specified config file and multi include exclude keywords:"
repomaestro gen --include-keywords aws,cli --exclude-keywords nodejs,couchdb --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/repoman.j2 --out-file ${STAGE_DIR}/repoman-filtered-multi.json
repomaestro gen --include-keywords aws,cli --exclude-keywords nodejs,couchdb --conf-file ${STAGE_DIR}/.repomaestro.yaml --template-file templates/vscode.j2 --out-file ${STAGE_DIR}/vscode-filtered-multi.json
