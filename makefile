MAKEFLAGS += --silent

verify:
	./scripts/verify.sh

update-api-spec:
	./scripts/update-api-spec.sh

generate-sdk:
	./scripts/generate-sdk.sh