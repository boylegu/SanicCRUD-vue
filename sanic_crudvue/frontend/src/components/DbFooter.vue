<template>
    <div class="container">
        <div class="footer-main"><p class="footer-main-title">{{ message }}</p><a
                href="https://github.com/ElemeFE/element/issues" target="_blank" class="footer-main-link">Feedback</a><a
                href="https://github.com/ElemeFE/element/blob/master/.github/CONTRIBUTING.en-US.md" target="_blank"
                class="footer-main-link">Contribution</a><a
                href="https://eleme.github.io/element-react/#/en-US/quick-start" target="_blank"
                class="footer-main-link">Element-React</a></div>

        <div class="layout-copy">
            <div class='d3'>
                <canvas id="myCanvas" width="80" height="120" style="background-color: transparent;"></canvas>
            </div>
            <p id="p1">2017 @gubaoer</p>
        </div>
        <div class="footer-social"></div>
    </div>

</template>

<script>

    import curvejs from 'curvejs'

    export default {
        data(){
            return {
                message: 'SanicCRUD-vue_0.1 By BoyleGu',
            }
        },

        mounted (){

            const {Stage, Curve, motion} = curvejs;

            let canvas = document.getElementById('myCanvas'),
                stage = new Stage(canvas);

            let curve = new Curve({
                color: '#ffaeac',
                data: {value: 0, step: 0.01, width: 90, height: 80},
                motion: motion.noise
            });
            stage.add(curve);

            function tick() {

                stage.update();
                requestAnimationFrame(tick)
            }

            tick()
        },

    }
</script>

<style scoped>
    .container {
        width: 1140px;
        padding: 0 30px;
        margin: 0 auto;
    }

    .footer-main {
        font-size: 0;
        padding-top: 40px;
        display: inline-block;
    }

    .footer-main .footer-main-title {
        line-height: 1;
        font-size: 22px;
        margin: 0;
    }

    .footer-main .footer-main-link {
        display: inline-block;
        margin: 12px 18px 0 0;
        line-height: 1;
        font-size: 12px;
        color: #768193;
    }

    .layout-copy p {
        width: 100%;
        display: inline-block;
        text-align: center;
        position: relative;
        top: -142px;
        font-size: 12px;

    }

    .d3 {
        width: 100%;
        display: inline-block;
        text-align: center;
        position: relative;
        top: -80px;
    }


</style>