<template>
  <vl-map :load-tiles-while-animating="true" :load-tiles-while-interacting="true" style="height: 800px">
      <vl-view :zoom.sync="zoom" :center.sync="center" :rotation.sync="rotation"></vl-view>

      <vl-layer-tile id="osm">
          <vl-source-osm></vl-source-osm>
      </vl-layer-tile>
      <vl-layer-tile>
          <vl-source-xyz url="http://anka:9090/{z}/{x}/{y}.png"></vl-source-xyz>
      </vl-layer-tile>
  </vl-map>
</template>

<script>

  export default {
    data () {
      return { 
        zoom: 0,
        center: [0, 0],
        rotation: 0
      }
    }
  }
</script>
