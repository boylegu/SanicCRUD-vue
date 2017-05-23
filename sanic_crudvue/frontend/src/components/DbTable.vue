<template>
    <div>
        <el-table
                :data="tableData"
                border
                style="width: 100%"
                class="table">
            <el-table-column
                    fixed
                    prop="id"
                    label="item_id"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="server_type"
                    label="server_type"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="server_id"
                    label="server_id"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="config_name"
                    label="config_name"
                    width="130">
            </el-table-column>
            <el-table-column
                    prop="warning"
                    label="warning"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="critical"
                    label="critical"
                    width="100">
            </el-table-column>
            <el-table-column
                    prop="description"
                    label="description"
                    width="300">
            </el-table-column>
            <el-table-column
                    fixed="right"
                    label="操作"
                    width="100">
                <template scope="scope">
                    <el-button @click="editItem(scope.$index, tableData)" type="text" size="large">编辑</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination class="pagination" layout="prev, pager, next" :total="total" :page-size="pageSize"
                       v-on:current-change="changePage">
        </el-pagination>
        <db-modal :dialogFormVisible="dialogFormVisible" :form="form" v-on:canclemodal="dialogVisible"></db-modal>
    </div>

</template>

<script>
    import axios from 'axios'
    import Bus from '../eventBus'
    import DbModal from './DbModal.vue'

    export default {
        data(){
            return {
                tableData: [],
                apiUrl: 'http://127.0.0.1:8000/xxx/core/api/config-list',
                total: 0,
                pageSize: 10,
                currentPage: 1,
                server_type: '',
                description: '',
                dialogFormVisible: false,
                form: '',
            }
        },
        components: {
            DbModal
        },
        mounted () {
            this.getCustomers();
            Bus.$on('filterResultData', (data) => {
                this.tableData = data.results;
                this.total = data.total;
                this.pageSize = data.count;
                this.description = data.description;
                this.server_type = data.server_type;

            });
        },

        methods: {

            dialogVisible: function () {
                this.dialogFormVisible = false;
            },

            getCustomers: function () {
                axios.get(this.apiUrl, {
                    params: {
                        page: this.currentPage,
                        server_type: this.server_type,
                        description: this.description
                    }
                }).then((response) => {
                    this.tableData = response.data.results;
                    this.total = response.data.total;
                    this.pageSize = response.data.count;
                    console.log(response.data);
                }).catch(function (response) {
                    console.log(response)
                });
            },
            changePage: function (currentPage) {
                this.currentPage = currentPage;
                this.getCustomers()
            },
            editItem: function (index, rows) {
                this.dialogFormVisible = true;
                const itemId = rows[index].id;
                const idurl = 'http://127.0.0.1:8000/xxxx/core/api/config-detail/' + itemId;
                axios.get(idurl).then((response) => {
                    this.form = response.data;
                }).catch(function (response) {
                    console.log(response)
                });
            },
        }
    }
</script>

<style>
    .table {
        margin-top: 30px;
    }

    .pagination {
        margin-top: 10px;
        float: right;
    }

</style>