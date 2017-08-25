import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

const DbFilterinput = resolve => require(['./components/DbFilterinput.vue'], resolve);
const DbTable = resolve => require(['./components/Dbtable.vue'], resolve);

const DbMap = resolve => require(['./components/DbMap.vue'], resolve);

export default new Router({
        //mode: 'history',
        routes: [
            {
                path: '/dashboard', components: {
                one: DbFilterinput,
                two: DbTable
            },
            },
            {
                path: '/map', components: {
                one: DbMap
            }
            }
        ]

    }
)