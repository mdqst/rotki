<script setup lang="ts">
const props = defineProps<{
  source: string;
  iconUrl?: string;
  icon?: string;
}>();

const { getAirdropName, getAirdropImageUrl, loading } = useAirdropsMetadata();

const { source, icon } = toRefs(props);

const name = getAirdropName(source);
const image = getAirdropImageUrl(source);
const imageFromIconName = computed(() => {
  const iconVal = get(icon);
  if (!iconVal)
    return undefined;

  return `./assets/images/protocols/${iconVal}`;
});
</script>

<template>
  <div class="flex items-center gap-4">
    <AdaptiveWrapper>
      <AppImage
        :src="iconUrl || imageFromIconName || image"
        width="1.5rem"
        height="1.5rem"
        contain
        :loading="loading"
        max-height="2rem"
        max-width="2rem"
      />
    </AdaptiveWrapper>
    <div>{{ name }}</div>
  </div>
</template>
