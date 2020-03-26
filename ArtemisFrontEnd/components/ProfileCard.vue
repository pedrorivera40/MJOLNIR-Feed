<template>
    <v-card class="mx-auto" max-width="400">
        
        <v-card-title hover='true'>
        <v-container>
            <v-row>
                <v-col cols='12'>
                    <v-avatar size="100" class="mx-auto">
                        <img
                            :src="img"
                            alt="Developer"
                            height="200px"
                        >
                    </v-avatar>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='12'>{{name}}</v-col>
            </v-row>
        </v-container>
        </v-card-title>
        <v-card-text class="text--primary">
        <div>{{bio}}</div>
        </v-card-text>
    
    </v-card>
</template>

<script>
export default {
props:{
name: String,
img: String,
bio: String,
}
};
</script>

<style>
</style>

