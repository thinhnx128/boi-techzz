## feat(vue): Add `@tryabby/vue` Integration (`useAbby`, `useFeatureFlag`, `useRemoteConfig`)

### Summary
Implements the Vue 3 / Nuxt composable integration inside `packages/vue` (`@tryabby/vue`) as requested in #68:
- `useAbby(testId)`: Returns reactive `variant` and `onAct` handler consuming `@tryabby/core`.
- `useFeatureFlag(flagKey)`: Returns reactive boolean value for feature flags.
- `useRemoteConfig(configKey)`: Returns typed reactive remote configuration value.
- Includes unit and type tests in `packages/vue/test/index.test.ts`.

### Reference Package
https://github.com/thinhnx128/boi-tech-ai-bounties/tree/main/packages/tryabby-vue-integration-68

/claim #68
Fixes #68