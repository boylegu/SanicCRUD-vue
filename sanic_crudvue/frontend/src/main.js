/**
 * Created by gubaoer on 17/4/18.
 */

import Vue from 'vue'
import {
    Button,
    Select,
    Row,
    Col,
    Pagination,
    Table,
    TableColumn,
    Form,
    FormItem,
    Input,
    Dialog,
    Option
} from 'element-ui'
import App from './App.vue'
import 'element-ui/lib/theme-default/index.css'


Vue.use(Button);
Vue.use(Select);
Vue.use(Row);
Vue.use(Col);
Vue.use(Pagination);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Input);
Vue.use(Dialog);
Vue.use(Option);

// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    render: h => h(App)
});