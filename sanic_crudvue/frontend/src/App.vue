<template>
    <div class="wrapper">
        <db-header></db-header>
        <el-row class="container">
            <el-col :span="4" class="menu">
                <db-sidebar></db-sidebar>
            </el-col>
            <el-col :span="20" class="content">
                <db-filterinput></db-filterinput>
                <db-table></db-table>

            </el-col>
        </el-row>
    </div>
</template>

<script>

    import DbHeader  from './components/DbHeader.vue'
    import DbSidebar from './components/DbSidebar.vue'
    import DbFilterinput from './components/DbFilterinput.vue'
    import DbTable from './components/DbTable.vue'

    export default {
        name: 'app',
        components: {
            DbHeader,
            DbSidebar,
            DbFilterinput,
            DbTable,
        },
    }

</script>

<style>

    element.style {
        background-color: rgb(10, 47, 88);
    }

    body {
        font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
        margin: 0;
    }

    .el-menu, body, html {
        height: 100%;
    }

    .wrapper {

        position: relative;
    }

    div {
        display: block;
    }

    .container {
        padding-top: 70px;
    }

    .container, .wrapper {
        height: 100%;
    }

    .menu {
        height: 100%;
        background-color: #eef1f6;
    }

    .content {
        padding: 25px;
    }

</style>