<template>
    <el-form :inline="true" :model="formInline">

        <el-form-item label="类型">
            <el-select v-model="formInline.server_type" clearable placeholder="请选择类型"
                       v-on:visible-change="selectDemo">
                <el-option
                        v-for="item in type_options"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
        </el-form-item>

        <el-form-item v-if='formInline.server_type' label="Description">
            <el-input v-model="formInline.description" placeholder="请输入相关描述"></el-input>
        </el-form-item>

        <el-form-item v-else='formInline.server_type' label="Description">
            <el-input v-model="formInline.description" disabled placeholder="请输入相关描述"></el-input>
        </el-form-item>

    </el-form>
</template>

<script>
    import axios from 'axios'
    import lodash from 'lodash'
    import Bus from '../eventBus'

    export default {
        name: 'db-filterinput',
        data() {
            return {
                type_options: [],
                formInline: {
                    server_type: '',
                    description: ''
                },
                formLabelWidth: '120px'
            }
        },

        watch: {
            'formInline.server_type': 'filterResultData',
            'formInline.description': 'filterResultData'
        },

        methods: {
            selectDemo: function (params) {
                if (params) {
                    axios.get("http://127.0.0.1:8000/xxxx/core/api/all-servertype")
                        .then((response) => {
                            this.type_options = response.data;
                            console.log(response.data);
                        }).catch(function (response) {
                        console.log(response)
                    });
                }

            },
            filterResultData: _.debounce(
                function () {
                    axios.get("http://127.0.0.1:8000/xxx/core/api/config-list", {
                        params: {
                            server_type: this.formInline.server_type,
                            description: this.formInline.description
                        }
                    }).then((response) => {
                        response.data['server_type'] = this.formInline.server_type;
                        response.data['description'] = this.formInline.description;
                        Bus.$emit('filterResultData', response.data);
                        console.log(response.data);
                    }).catch(function (response) {
                        console.log(response)
                    });

                },
                500
            ),
        }
    }


</script>