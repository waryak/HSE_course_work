from django.contrib import admin

from blockchain.models.blockchain import Blockchain
from blockchain.models.contract import Contract
from blockchain.models.node import Node


class NodeInline(admin.TabularInline):
    model = Node
    fields = 'title', 'queue_name',
    extra = 1


class ContractInline(admin.TabularInline):
    model = Contract
    fields = 'title', 'source',
    extra = 1


@admin.register(Blockchain)
class BlockchainAdmin(admin.ModelAdmin):
    list_display = 'title',
    search_fields = 'title',
    inlines = NodeInline, ContractInline,
