<script setup lang="ts" generic="T extends object">
import type { Collection } from '@/types/collection';

const props = defineProps<{
  collection: Collection<T>;
}>();

const emit = defineEmits<{
  (e: 'set-page', page: number): void;
}>();

function setPage(page: number) {
  emit('set-page', page);
}

const { collection } = toRefs(props);

const { data, limit, found, total, entriesFoundTotal, totalValue } = getCollectionData(collection);

const { itemsPerPage } = storeToRefs(useFrontendSettingsStore());
watch([data, found, itemsPerPage], ([data, found, itemsPerPage]) => {
  if (data.length === 0 && found > 0) {
    const lastPage = Math.ceil(found / itemsPerPage);
    setPage(lastPage);
  }
});

const { showUpgradeRow, itemLength } = setupEntryLimit(limit, found, total, entriesFoundTotal);
</script>

<template>
  <div>
    <slot
      :data="data"
      :limit="limit"
      :found="found"
      :total="total"
      :entries-found-total="entriesFoundTotal"
      :total-value="totalValue"
      :item-length="itemLength"
      :show-upgrade-row="showUpgradeRow"
    />
  </div>
</template>
