# This file contains minimized db schema and it should not be touched manually but only generated by tools/scripts/generate_minimized_db_schema.py
# Created at 2024-12-02 14:23:21 UTC with rotki version 1.36.2.dev62+g6c565534a by nicholas
MINIMIZED_USER_DB_SCHEMA = {
    "trade_type": "typechar(1)primarykeynotnull,seqintegerunique",
    "location": "locationchar(1)primarykeynotnull,seqintegerunique",
    "asset_movement_category": "categorychar(1)primarykeynotnull,seqintegerunique",
    "balance_category": "categorychar(1)primarykeynotnull,seqintegerunique",
    "assets": "identifiertextnotnullprimarykey",
    "timed_balances": "categorychar(1)notnulldefault('a')referencesbalance_category(category),timestampinteger,currencytext,amounttext,usd_valuetext,foreignkey(currency)referencesassets(identifier)onupdatecascade,primarykey(timestamp,currency,category)",
    "timed_location_data": "timestampinteger,locationchar(1)notnulldefault('a')referenceslocation(location),usd_valuetext,primarykey(timestamp,location)",
    "user_credentials": "nametextnotnull,locationchar(1)notnulldefault('a')referenceslocation(location),api_keytext,api_secrettext,passphrasetext,primarykey(name,location)",
    "user_credentials_mappings": "credential_nametextnotnull,credential_locationchar(1)notnulldefault('a')referenceslocation(location),setting_nametextnotnull,setting_valuetextnotnull,foreignkey(credential_name,credential_location)referencesuser_credentials(name,location)ondeletecascadeonupdatecascade,primarykey(credential_name,credential_location,setting_name)",
    "external_service_credentials": "namevarchar[30]notnullprimarykey,api_keytextnotnull,api_secrettext",
    "blockchain_accounts": "blockchainvarchar[24]notnull,accounttextnotnull,primarykey(blockchain,account)",
    "evm_accounts_details": "accountvarchar[42]notnull,chain_idintegernotnull,keytextnotnull,valuetextnotnull,primarykey(account,chain_id,key,value)",
    "multisettings": "namevarchar[24]notnull,valuetext,unique(name,value)",
    "manually_tracked_balances": "idintegerprimarykey,assettextnotnull,labeltextnotnull,amounttext,locationchar(1)notnulldefault('a')referenceslocation(location),categorychar(1)notnulldefault('a')referencesbalance_category(category),foreignkey(asset)referencesassets(identifier)onupdatecascade",
    "trades": "idtextprimarykeynotnull,timestampintegernotnull,locationchar(1)notnulldefault('a')referenceslocation(location),base_assettextnotnull,quote_assettextnotnull,typechar(1)notnulldefault('a')referencestrade_type(type),amounttextnotnull,ratetextnotnull,feetext,fee_currencytext,linktext,notestext,foreignkey(base_asset)referencesassets(identifier)onupdatecascade,foreignkey(quote_asset)referencesassets(identifier)onupdatecascade,foreignkey(fee_currency)referencesassets(identifier)onupdatecascade",
    "evm_transactions": "identifierintegernotnullprimarykey,tx_hashblobnotnull,chain_idintegernotnull,timestampintegernotnull,block_numberintegernotnull,from_addresstextnotnull,to_addresstext,valuetextnotnull,gastextnotnull,gas_pricetextnotnull,gas_usedtextnotnull,input_datablobnotnull,nonceintegernotnull,unique(tx_hash,chain_id)",
    "optimism_transactions": "tx_idintegernotnullprimarykey,l1_feetext,foreignkey(tx_id)referencesevm_transactions(identifier)ondeletecascadeonupdatecascade",
    "evm_internal_transactions": "parent_txintegernotnull,trace_idintegernotnull,from_addresstextnotnull,to_addresstext,valuetextnotnull,foreignkey(parent_tx)referencesevm_transactions(identifier)ondeletecascadeonupdatecascade,primarykey(parent_tx,trace_id,from_address,to_address,value)",
    "evmtx_receipts": "tx_idintegernotnullprimarykey,contract_addresstext,statusintegernotnullcheck(statusin(0,1)),typeintegernotnull,foreignkey(tx_id)referencesevm_transactions(identifier)ondeletecascadeonupdatecascade",
    "evmtx_receipt_logs": "identifierintegernotnullprimarykey,tx_idintegernotnull,log_indexintegernotnull,datablobnotnull,addresstextnotnull,foreignkey(tx_id)referencesevmtx_receipts(tx_id)ondeletecascadeonupdatecascade,unique(tx_id,log_index)",
    "evmtx_receipt_log_topics": "logintegernotnull,topicblobnotnull,topic_indexintegernotnull,foreignkey(log)referencesevmtx_receipt_logs(identifier)ondeletecascadeonupdatecascade,primarykey(log,topic_index)",
    "evmtx_address_mappings": "tx_idintegernotnull,addresstextnotnull,foreignkey(tx_id)referencesevm_transactions(identifier)onupdatecascadeondeletecascade,primarykey(tx_id,address)",
    "zksynclite_tx_type": "typechar(1)primarykeynotnull,seqintegerunique",
    "zksynclite_transactions": "identifierintegernotnullprimarykey,tx_hashblobnotnullunique,typechar(1)notnulldefault('a')referenceszksynclite_tx_type(type),is_decodedintegernotnulldefault0check(is_decodedin(0,1)),timestampintegernotnull,block_numberintegernotnull,from_addresstextnotnull,to_addresstext,assettextnotnull,amounttextnotnull,feetext,foreignkey(asset)referencesassets(identifier)onupdatecascade",
    "zksynclite_swaps": "tx_idintegernotnull,from_assettextnotnull,from_amounttextnotnull,to_assettextnotnull,to_amounttext_notnull,foreignkey(tx_id)referenceszksynclite_transactions(identifier)onupdatecascadeondeletecascade,foreignkey(from_asset)referencesassets(identifier)onupdatecascade,foreignkey(to_asset)referencesassets(identifier)onupdatecascade",
    "margin_positions": "idtextprimarykey,locationchar(1)notnulldefault('a')referenceslocation(location),open_timeinteger,close_timeinteger,profit_losstext,pl_currencytextnotnull,feetext,fee_currencytext,linktext,notestext,foreignkey(pl_currency)referencesassets(identifier)onupdatecascade,foreignkey(fee_currency)referencesassets(identifier)onupdatecascade",
    "asset_movements": "idtextprimarykey,locationchar(1)notnulldefault('a')referenceslocation(location),categorychar(1)notnulldefault('a')referencesasset_movement_category(category),addresstext,transaction_idtext,timestampinteger,assettextnotnull,amounttext,fee_assettext,feetext,linktext,foreignkey(asset)referencesassets(identifier)onupdatecascade,foreignkey(fee_asset)referencesassets(identifier)onupdatecascade",
    "used_query_ranges": "namevarchar[24]notnullprimarykey,start_tsinteger,end_tsinteger",
    "evm_tx_mappings": "tx_idintegernotnull,valueintegernotnull,foreignkey(tx_id)referencesevm_transactions(identifier)onupdatecascadeondeletecascade,primarykey(tx_id,value)",
    "settings": "namevarchar[24]notnullprimarykey,valuetext",
    "tags": "nametextnotnullprimarykeycollatenocase,descriptiontext,background_colortext,foreground_colortext",
    "tag_mappings": "object_referencetext,tag_nametext,foreignkey(tag_name)referencestags(name)primarykey(object_reference,tag_name)",
    "xpubs": "xpubtextnotnull,derivation_pathtextnotnull,labeltext,blockchaintextnotnull,primarykey(xpub,derivation_path,blockchain)",
    "xpub_mappings": "addresstextnotnull,xpubtextnotnull,derivation_pathtextnotnull,account_indexinteger,derived_indexinteger,blockchaintextnotnull,foreignkey(blockchain,address)referencesblockchain_accounts(blockchain,account)ondeletecascadeforeignkey(xpub,derivation_path,blockchain)referencesxpubs(xpub,derivation_path,blockchain)ondeletecascadeprimarykey(address,xpub,derivation_path,blockchain)",
    "eth2_validators": "identifierintegernotnullprimarykey,validator_indexintegerunique,public_keytextnotnullunique,ownership_proportiontextnotnull,withdrawal_addresstext,activation_timestampinteger,withdrawable_timestampinteger,exited_timestampinteger",
    "eth2_daily_staking_details": "validator_indexintegernotnull,timestampintegernotnull,pnltextnotnull,foreignkey(validator_index)referenceseth2_validators(validator_index)onupdatecascadeondeletecascade,primarykey(validator_index,timestamp)",
    "history_events": "identifierintegernotnullprimarykey,entry_typeintegernotnull,event_identifiertextnotnull,sequence_indexintegernotnull,timestampintegernotnull,locationchar(1)notnulldefault('a')referenceslocation(location),location_labeltext,assettextnotnull,amounttextnotnull,usd_valuetextnotnull,notestext,typetextnotnull,subtypetextnotnull,extra_datatext,foreignkey(asset)referencesassets(identifier)onupdatecascade,unique(event_identifier,sequence_index)",
    "evm_events_info": "identifierintegerprimarykey,tx_hashblobnotnull,counterpartytext,producttext,addresstext,foreignkey(identifier)referenceshistory_events(identifier)onupdatecascadeondeletecascade",
    "eth_staking_events_info": "identifierintegerprimarykey,validator_indexintegernotnull,is_exit_or_blocknumberintegernotnull,foreignkey(identifier)referenceshistory_events(identifier)onupdatecascadeondeletecascade",
    "history_events_mappings": "parent_identifierintegernotnull,nametextnotnull,valueintegernotnull,foreignkey(parent_identifier)referenceshistory_events(identifier)onupdatecascadeondeletecascade,primarykey(parent_identifier,name,value)",
    "action_type": "typechar(1)primarykeynotnull,seqintegerunique",
    "ignored_actions": "typechar(1)notnulldefault('a')referencesaction_type(type),identifiertext,primarykey(type,identifier)",
    "nfts": "identifiertextnotnullprimarykey,nametext,last_pricetextnotnull,last_price_assettextnotnull,manual_priceintegernotnullcheck(manual_pricein(0,1)),owner_addresstext,blockchaintextgeneratedalwaysas('eth')virtual,is_lpintegernotnullcheck(is_lpin(0,1)),image_urltext,collection_nametext,usd_pricerealnotnulldefault0,foreignkey(blockchain,owner_address)referencesblockchain_accounts(blockchain,account)ondeletecascade,foreignkey(identifier)referencesassets(identifier)onupdatecascade,foreignkey(last_price_asset)referencesassets(identifier)onupdatecascade",
    "ens_mappings": "addresstextnotnullprimarykey,ens_nametextunique,last_updateintegernotnull,last_avatar_updateintegernotnulldefault0",
    "address_book": "addresstextnotnull,blockchaintextnotnull,nametextnotnull,primarykey(address,blockchain)",
    "rpc_nodes": "identifierintegernotnullprimarykey,nametextnotnull,endpointtextnotnull,ownedintegernotnullcheck(ownedin(0,1)),activeintegernotnullcheck(activein(0,1)),weighttextnotnull,blockchaintextnotnull,unique(endpoint,blockchain)",
    "user_notes": "identifierintegernotnullprimarykey,titletextnotnull,contenttextnotnull,locationtextnotnull,last_update_timestampintegernotnull,is_pinnedintegernotnullcheck(is_pinnedin(0,1))",
    "skipped_external_events": "identifierintegernotnullprimarykey,datatextnotnull,locationchar(1)notnulldefault('a')referenceslocation(location),extra_datatext,unique(data,location)",
    "accounting_rules": "identifierintegernotnullprimarykey,typetextnotnull,subtypetextnotnull,counterpartytextnotnull,taxableintegernotnullcheck(taxablein(0,1)),count_entire_amount_spendintegernotnullcheck(count_entire_amount_spendin(0,1)),count_cost_basis_pnlintegernotnullcheck(count_cost_basis_pnlin(0,1)),accounting_treatmenttext,unique(type,subtype,counterparty)",
    "linked_rules_properties": "identifierintegerprimarykeynotnull,accounting_ruleintegerreferencesaccounting_rules(identifier),property_nametextnotnull,setting_nametextnotnullreferencessettings(name)",
    "unresolved_remote_conflicts": "identifierintegerprimarykeynotnull,local_idintegernotnull,remote_datatextnotnull,typeintegernotnull",
    "key_value_cache": "nametextnotnullprimarykey,valuetext",
    "calendar": "identifierintegerprimarykeynotnull,nametextnotnull,timestampintegernotnull,descriptiontext,counterpartytext,addresstext,blockchaintext,colortext,auto_deleteintegernotnullcheck(auto_deletein(0,1)),foreignkey(blockchain,address)referencesblockchain_accounts(blockchain,account)ondeletecascade,unique(name,address,blockchain)",
    "calendar_reminders": "identifierintegerprimarykeynotnull,event_idintegernotnull,secs_beforeintegernotnull,foreignkey(event_id)referencescalendar(identifier)ondeletecascade",
    "cowswap_orders": "identifiertextnotnullprimarykey,order_typetextnotnull,raw_fee_amounttextnotnull",
    "gnosispay_data": "identifierintegerprimarykeynotnull,tx_hashblobnotnullunique,timestampintegernotnull,merchant_nametextnotnull,merchant_citytext,countrytextnotnull,mccintegernotnull,transaction_symboltextnotnull,transaction_amounttextnotnull,billing_symboltext,billing_amounttext,reversal_symboltext,reversal_amounttext,reversal_tx_hashblobunique",
}
