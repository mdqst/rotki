<script setup lang="ts">
import { some } from 'lodash-es';
import { isEvmNativeToken } from '@/types/asset';
import type { AssetBalance, AssetBalanceWithBreakdown } from '@/types/balances';
import type { Nullable } from '@rotki/common';
import type { DataTableColumn, DataTableSortData } from '@rotki/ui-library';

defineOptions({
  name: 'AssetBalances',
});

const search = defineModel<string>('search', { required: false, default: '' });

const props = withDefaults(
  defineProps<{
    balances: AssetBalanceWithBreakdown[];
    details?: {
      groupId: string;
      chains: string[];
    };
    loading?: boolean;
    hideTotal?: boolean;
    hideBreakdown?: boolean;
    stickyHeader?: boolean;
    isLiability?: boolean;
    allBreakdown?: boolean;
  }>(),
  {
    loading: false,
    hideTotal: false,
    hideBreakdown: false,
    stickyHeader: false,
    details: undefined,
    isLiability: false,
    allBreakdown: false,
  },
);

const { t } = useI18n();

const { balances } = toRefs(props);
const expanded = ref<AssetBalanceWithBreakdown[]>([]);

const sort = ref<DataTableSortData<AssetBalanceWithBreakdown>>({
  column: 'value',
  direction: 'desc' as const,
});

const { assetSymbol, assetName, assetInfo } = useAssetInfoRetrieval();
const { currencySymbol } = storeToRefs(useGeneralSettingsStore());

const isExpanded = (asset: string) => some(get(expanded), { asset });

function expand(item: AssetBalanceWithBreakdown) {
  set(expanded, isExpanded(item.asset) ? [] : [item]);
}

function getAssets(item: AssetBalanceWithBreakdown): string[] {
  return item.breakdown?.map(entry => entry.asset) ?? [];
}

function assetFilter(item: Nullable<AssetBalance>) {
  return assetFilterByKeyword(item, get(search), assetName, assetSymbol);
}

const filteredBalances = computed(() => get(balances).filter(assetFilter));

const total = computed(() => bigNumberSum(get(filteredBalances).map(({ value }) => value)));

const cols = computed<DataTableColumn<AssetBalanceWithBreakdown>[]>(() => [
  {
    label: t('common.asset'),
    key: 'asset',
    class: 'text-no-wrap w-full',
    cellClass: 'py-0',
    sortable: true,
  },
  {
    label: t('common.price_in_symbol', {
      symbol: get(currencySymbol),
    }),
    key: 'price',
    align: 'end',
    cellClass: 'py-0',
    sortable: true,
  },
  {
    label: t('common.amount'),
    key: 'amount',
    align: 'end',
    cellClass: 'py-0',
    sortable: true,
  },
  {
    label: t('common.value_in_symbol', {
      symbol: get(currencySymbol),
    }),
    key: 'value',
    align: 'end',
    class: 'text-no-wrap',
    cellClass: 'py-0',
    sortable: true,
  },
]);

const sorted = computed<AssetBalanceWithBreakdown[]>(() => sortAssetBalances([...get(filteredBalances)], get(sort), assetInfo));
</script>

<template>
  <RuiDataTable
    v-model:sort.external="sort"
    :cols="cols"
    :rows="sorted"
    :loading="loading"
    :expanded="expanded"
    :loading-text="t('asset_balances.loading')"
    :empty="{ description: t('data_table.no_data') }"
    :sticky-header="stickyHeader"
    row-attr="asset"
    single-expand
    outlined
    dense
  >
    <template #item.asset="{ row }">
      <AssetDetails
        opens-details
        :asset="row.asset"
        :is-collection-parent="!!row.breakdown"
      />
    </template>
    <template #item.price="{ row }">
      <AmountDisplay
        :loading="!row.price || row.price.lt(0)"
        no-scramble
        show-currency="symbol"
        :price-asset="row.asset"
        :price-of-asset="row.price"
        :fiat-currency="currencySymbol"
        :value="row.price"
      />
    </template>
    <template #item.amount="{ row }">
      <AmountDisplay :value="row.amount " />
    </template>
    <template #item.value="{ row }">
      <AmountDisplay
        show-currency="symbol"
        :amount="row.amount"
        :fiat-currency="currencySymbol"
        :value="row.value"
        :loading="row.price.lt(0)"
      />
    </template>
    <template
      v-if="balances.length > 0 && !hideTotal"
      #body.append
    >
      <RowAppend
        label-colspan="3"
        :label="t('common.total')"
        :is-mobile="false"
        :right-patch-colspan="2"
        class-name="[&>td]:p-4 text-sm"
      >
        <AmountDisplay
          :fiat-currency="currencySymbol"
          show-currency="symbol"
          :value="total"
          :loading="loading || total.eq(0)"
        />
      </RowAppend>
    </template>
    <template #expanded-item="{ row }">
      <EvmNativeTokenBreakdown
        v-if="!hideBreakdown && isEvmNativeToken(row.asset)"
        :blockchain-only="!allBreakdown"
        :assets="getAssets(row)"
        :details="details"
        :identifier="row.asset"
        :is-liability="isLiability"
        class="bg-white dark:bg-[#1E1E1E] my-2"
      />
      <AssetBalances
        v-else
        v-bind="props"
        hide-total
        :balances="row.breakdown ?? []"
        :sticky-header="false"
        :is-liability="isLiability"
        :all-breakdown="allBreakdown"
        class="bg-white dark:bg-[#1E1E1E] my-2"
      />
    </template>
    <template #item.expand="{ row }">
      <RuiTableRowExpander
        v-if="row.breakdown || (!hideBreakdown && isEvmNativeToken(row.asset))"
        :expanded="isExpanded(row.asset)"
        @click="expand(row)"
      />
    </template>
  </RuiDataTable>
</template>
