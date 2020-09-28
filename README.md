# ecs-desired-count

![Status](https://github.com/theuves/ecs-desired-count/workflows/Test/badge.svg)

> AWS Lambda to update the 'desired count' of a ECS service.

## Installation

```bash
git clone https://github.com/theuves/ecs-desired-count.git
cd ecs-desired-count
npm install
```

## Configuration

Create a `.env` file with the following environment variables:

- `REGION` - AWS region where the lambda will be deployed (e.g. `us-east-1`)
- `ECS_CLUSTER` - cluster name
- `ECS_SERVICE` - service name
- `COUNT_ORDER` - list of desired counts separated by commas (e.g. `0,1`)

### The `COUNT_ORDER` variable

If the value of `COUNT_ORDER` is `2,4,6` and the current desired count is 2 then the desired count will be 4 on the first run, 6 on the second, 2 on the third and so on.

## Deploy

```bash
serverless deploy
```

Use `serverless remove` to remove Serverless service.

## Requirements

- [Serverless Framework](https://www.serverless.com/)

## License

MIT &copy; Matheus Alves
