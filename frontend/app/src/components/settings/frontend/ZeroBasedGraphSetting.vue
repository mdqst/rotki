<script setup lang="ts">
const zeroBased = ref<boolean>(false);
const { graphZeroBased: enabled } = storeToRefs(useFrontendSettingsStore());

onMounted(() => {
  set(zeroBased, get(enabled));
});

const { t } = useI18n();
</script>

<template>
  <div class="pb-2">
    <SettingsOption
      #default="{ error, success, update }"
      setting="graphZeroBased"
      frontend-setting
    >
      <RuiSwitch
        v-model="zeroBased"
        class="general-settings__fields__zero-base"
        :label="t('frontend_settings.graph_basis.zero_based.label')"
        :hint="t('frontend_settings.graph_basis.zero_based.hint')"
        :success-messages="success"
        :error-messages="error"
        color="primary"
        @update:model-value="update($event)"
      />
    </SettingsOption>
  </div>
</template>
