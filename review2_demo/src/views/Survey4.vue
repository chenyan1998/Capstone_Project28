<template>
    <v-container>
      <v-row>
        <v-col
          v-for="(item, i) in items"
          :key="i"
          cols="6"
        >
          <v-card
            :color="item.color"
            dark
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title
                  class="headline"
                  v-text="item.title"
                ></v-card-title>

                <v-card-subtitle v-text="item.artist"></v-card-subtitle>

                <v-card-actions>
                  <v-btn
                    color="primary"
                    class="mr-10"
                    rel="noopener"
                    target="_blank"
                  >
                    Send
                  </v-btn>
                  <v-btn
                  >
                    Report
                  </v-btn>
                </v-card-actions>
                
              </div>

              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src="item.src"></v-img>
              </v-avatar>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>
<script>
  export default {
    data: () => ({
      items: [
        {
          color: 'success',
          // src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
          title: 'Personality Survey',
          artist: 'Learn about employees\' personality',
        },
        {
          color: 'info',
          // src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
          title: 'Physical Wellbeing',
          artist: 'Physical fitness is the first requisite of happiness',
        },
        {
          color: 'warning lighten-2',
          // src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
          title: 'Sentiment Analysis',
          artist: 'How employees interact with people',
        },
        {
          color: 'teal',
          src: '../assets/register.jpg',
          title: 'Personal Information',
          artist: 'Individual differences including past work experiences etc.',
        },
      ],
    }),
  }
</script>
