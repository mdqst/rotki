<script lang="ts" setup>
import { Defaults } from '@/data/defaults';

const { t } = useI18n();
const ksmRpcEndpoint = ref(Defaults.KSM_RPC_ENDPOINT);

const { ksmRpcEndpoint: ksmRpc } = storeToRefs(useGeneralSettingsStore());

function ksmSuccessMessage(endpoint: string) {
  if (endpoint) {
    return t('general_settings.validation.ksm_rpc.success_set', {
      endpoint,
    });
  }
  return t('general_settings.validation.ksm_rpc.success_unset');
}

onBeforeMount(() => {
  set(ksmRpcEndpoint, get(ksmRpc) || Defaults.KSM_RPC_ENDPOINT);
});
</script>

<template>
  <SettingsOption
    #default="{ error, success, update }"
    setting="ksmRpcEndpoint"
    :error-message="t('general_settings.validation.ksm_rpc.error')"
    :success-message="ksmSuccessMessage"
  >
    <RuiTextField
      v-model="ksmRpcEndpoint"
      variant="outlined"
      color="primary"
      class="general-settings__fields__ksm-rpc-endpoint pt-2"
      :label="t('general_settings.labels.ksm_rpc_endpoint')"
      type="text"
      :success-messages="success"
      :error-messages="error"
      clearable
      @paste="update($event.clipboardData.getData('text'))"
      @click:clear="update('')"
      @update:model-value="update($event)"
    />
  </SettingsOption>
</template>
