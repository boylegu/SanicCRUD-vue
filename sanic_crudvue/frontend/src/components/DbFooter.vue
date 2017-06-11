<template>
    <div class="container">
        <div class="footer-main"><p class="footer-main-title">{{ message }}</p><a
                href="https://github.com/boylegu/SanicCRUD-vue" target="_blank" class="footer-main-link">Github</a><a
                href="https://github.com/ElemeFE/element/blob/master/.github/CONTRIBUTING.en-US.md" target="_blank"
                class="footer-main-link">Email</a><a
                href="https://github.com/ElemeFE/element/blob/master/.github/CONTRIBUTING.en-US.md" target="_blank"
                class="footer-main-link">License</a></div>

        <div class="layout-copy elementdoc">

            <i class="elementdoc">
                <canvas id="myCanvas" width="80" height="80" style="background-color: transparent;"></canvas>
            </i>
            <i class="elementdoc">2017 @ Boyle.Gu 顾鲍尔. Commemorate the 6 anniversary of enter the profession </i>
        </div>

        <div class="footer-social">

            <div class="footer-popover" style="width: 120px; display: none;">
                <div class="footer-popover-title">饿了么 UED</div>
                <img src="static/qrcode.a88f522.png" alt="">
            </div>

            <i class="doc-icon-weixin elementdoc">

                <span>Thanks to:</span>
                <a class="rackspace">Python & JavaScript</a>

            </i>
            
            <i class="doc-icon-github elementdoc"></i>
        </div>

    </div>

</template>

<script>

    import curvejs from 'curvejs'

    export default {
        data(){
            return {
                message: 'SanicCRUD-Vue.js v0.1',
            }
        },

        mounted (){

            const {Stage, Curve, motion} = curvejs;

            let canvas = document.getElementById('myCanvas'),
                stage = new Stage(canvas);

            let curve = new Curve({
                color: '#ffaeac',
                data: {value: 0, step: 0.01, width: 80, height: 80},
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

    a {
        text-decoration: none;
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

    .layout-copy {
        display: inline-block;
        width: 570px;
        height: 80px;
        margin-left: 3px;
    }

    .layout-copy .elementdoc {
        display: inline-block;
        text-align: center;
        color: #8d99ab;
        width: 570px;
        vertical-align: middle;
        font-size: 12px;
    }

    .footer-social {
        float: right;
        line-height: 120px;
    }

    .footer-popover {
        padding: 0;
        min-width: 120px;
        line-height: normal;
        box-shadow: 0 0 11px 0 rgba(174, 187, 211, .24);
    }

    .elementdoc span {
        font-size: 14px;
        display: inline-block;
        position: relative;
        top: -28px;
        margin-right: 1px;

        padding-right: 12px;
        white-space: nowrap;
    }

    .elementdoc a {
        font-size: 14px;

    }



</style>