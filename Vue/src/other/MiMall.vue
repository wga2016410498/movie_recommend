<template>
    <TopBar/>
    <TopHeader/>
    <MenuAndSlideShow/>
    <HotSale/>
    <SiteFooter/>
</template>

<script>
import TopBar from '@/components/Mall/TopBar.vue'
import TopHeader from '@/components/Mall/TopHeader.vue';
import MenuAndSlideShow from '@/components/Mall/MenuAndSlideShow.vue';
import HotSale from '@/components/Mall/HotSale.vue';
import SiteFooter from '@/components/Mall/SiteFooter.vue';
export default {
    name:'mimall',
    components:{
        TopBar,
        TopHeader,
        MenuAndSlideShow,
        HotSale,
        SiteFooter,
    }
}
</script>

<style>

</style>