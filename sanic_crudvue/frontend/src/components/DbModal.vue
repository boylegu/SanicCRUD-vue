<template>
    <el-dialog title="编辑" v-model="dialogFormVisible" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="item_id" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.id" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="server_type" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.server_type" auto-complete="off"></el-input>
            </el-form-item>

            <el-form-item label="server_id" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.server_id" auto-complete="off"></el-input>
            </el-form-item>

            <el-form-item label="config_name" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.config_name" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="warning" :label-width="formLabelWidth">
                <el-input v-model="form.warning" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="critical" :label-width="formLabelWidth">
                <el-input v-model="form.critical" auto-complete="off"></el-input>
            </el-form-item>

            <el-form-item label="description" :label-width="formLabelWidth">
                <el-input :disabled="true" v-model="form.description" auto-complete="off"></el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button :plain="true" type="danger" v-on:click="canclemodal">取消</el-button>
            <el-button :plain="true" @click="updateForm(form)">保存</el-button>
        </div>
    </el-dialog>
</template>


<script>
    import axios from 'axios'

    export default {
        data(){
            return {
                formLabelWidth: '120px',
            }
        },
        props: ['dialogFormVisible', 'form'],

        methods: {
            updateForm: function (formName) {
                let itemId = formName.id;
                let server_id = formName.server_id;
                let server_type = formName.server_type;
                let config_name = formName.config_name;
                let warning = formName.warning;
                let critical = formName.critical;
                let description = formName.description;
                axios.put('http://127.0.0.1:8000/xxx/core/api/config-detail/' + itemId, {
                    config_name: config_name,
                    server_id: server_id,
                    server_type: server_type,
                    warning: warning,
                    critical: critical,
                    description: description
                })
                    .then(function (response) {
                        console.log(response);
                        this.form = response.data;

                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                location.reload();
            },
            canclemodal: function () {
                this.$emit('canclemodal');
            }
        }

    }

</script>