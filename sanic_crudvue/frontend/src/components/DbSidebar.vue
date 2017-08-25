<template>
    <el-menu default-active="0" class="el-menu-vertical-demo">
        <el-menu-item index="0">

            <router-link to="/dashboard"> {{menu1}} </router-link>

        </el-menu-item>
        <el-menu-item index="1">

            <router-link to="/map"> {{menu2}}</router-link>

        </el-menu-item>
    </el-menu>


</template>

<script>

    export default {
        name: 'db-sidebar',
        data() {
            return {
                menu1: 'Dashboard',
                menu2: 'Map'
            }
        },
    }

</script>

<style>
    li {
        padding-left: 20px;
    }
</style>
