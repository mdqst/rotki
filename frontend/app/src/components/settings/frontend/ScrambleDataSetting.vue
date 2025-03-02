<script setup lang="ts">
const { scrambleData: enabled, scrambleMultiplier: multiplier } = storeToRefs(useSessionSettingsStore());

const scrambleData = ref<boolean>(false);
const scrambleMultiplier = ref<string>('0');

const { t } = useI18n();

function randomMultiplier() {
  set(scrambleMultiplier, generateRandomScrambleMultiplier().toString());
}

function setData() {
  set(scrambleData, get(enabled));
  set(scrambleMultiplier, get(multiplier).toString());
}

onMounted(setData);

watch([enabled, multiplier], setData);
</script>

<template>
  <SettingsItem>
    <template #title>
      {{ t('frontend_settings.scramble.title') }}
    </template>

    <SettingsOption
      #default="{ error, success, update }"
      setting="scrambleData"
      session-setting
      :error-message="t('frontend_settings.scramble.validation.error')"
    >
      <RuiSwitch
        v-model="scrambleData"
        color="primary"
        class="general-settings__fields__scramble-data my-2"
        :label="t('frontend_settings.scramble.label')"
        :success-messages="success"
        :error-messages="error"
        @update:model-value="update($event)"
      />
    </SettingsOption>
    <SettingsOption
      #default="{ error, success, update }"
      setting="scrambleMultiplier"
      session-setting
    >
      <AmountInput
        v-model="scrambleMultiplier"
        class="general-settings__fields__scramble-multiplier"
        :label="t('frontend_settings.scramble.multiplier.label')"
        :hint="t('frontend_settings.scramble.multiplier.hint')"
        variant="outlined"
        :disabled="!scrambleData"
        :success-messages="success"
        :error-messages="error"
        @change="update($event)"
      >
        <template #append>
          <RuiButton
            variant="text"
            icon
            :disabled="!scrambleData"
            @click="randomMultiplier()"
          >
            <RuiIcon name="shuffle-line" />
          </RuiButton>
        </template>
      </AmountInput>
    </SettingsOption>
  </SettingsItem>
</template>
