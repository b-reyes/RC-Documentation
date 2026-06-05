# Alpine Hardware

On this page we provide users of Alpine a general overview of the hardware on Alpine as well as outline the various hardware that has been contributed by institutions. For more information on requesting these resources, please see [Alpine Slurm Directives](./alpine_slurm_directives.md) 

```{important}
All Alpine nodes are available to all users. For full details about node access, please read the [Alpine node access and FairShare policy](condo-fairshare-and-resource-access.md).
```

## University of Colorado Boulder contribution

:::{table}
:width: 95%
:widths: auto
:align: left


| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_ucb_total_64_core_256GB_cpu_nodes }} Milan General CPU | amilan              | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}         | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_128_core_256GB_cpu_nodes }} Milan CPU | amilan             | x86_64 AMD Milan | 2  | 128            | 1            |  {{ alpine_standard_ram_per_core }}         | N/A         | 0         | 416G SSD | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_48_core_1TB_cpu_nodes }} Milan High-Memory  | amem                | x86_64 AMD Milan | 2       | 48            | 1            | 21.5          | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amem                | x86_64 AMD Milan | 1       | 64            | 1            |  16           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_mi100_gpu_nodes }} Milan AMD GPU | ami100              | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_a100_gpu_nodes }} Milan NVIDIA GPU    | aa100               | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_gh200_gpu_nodes }} Grace CPU NVIDIA Hopper GPU    | gh200<br><br>Note: these nodes are only available upon request, please submit a [support request form](https://colorado.service-now.com/req_portal?id=ucb_sc_rc_form). | ARM Neoverse V2 | 1       | 72            | 1            |  6.6          | NVIDIA Hopper GPU | 1         | 1.8 T SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_acompile_nodes }} Milan CPU compile nodes | acompile | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_64_core_256GB_cpu_nodes_atesting }} Milan CPU test nodes; pulls from CU amilan pool | atesting | x86_64 AMD Milan | 1 or 2  | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_ucb_total_atesting_a100_gpu_nodes }} Milan NVIDIA GPU testing node | atesting_a100 | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3 (each split by MIG)        | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_ucb_total_atesting_mi100_gpu_nodes }} Milan AMD GPU testing nodes; pulls from ami100 pool | atesting_mi100 | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | AMD MI100   | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |

:::

## CU Anschutz Medical Campus contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_amc_total_64_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 1       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_amc_total_64_core_1TB_cpu_nodes }} Milan High-Memory   | amem           | x86_64 AMD Milan | 1       | 64            | 1            |  16          | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 
| {{ alpine_amc_total_128_core_2TB_cpu_nodes }} Milan High-Memory   | amem           | x86_64 AMD Milan | 2       | 128           | 1            |  16           | N/A         | 0         |  70G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) | 
| {{ alpine_amc_total_a100_gpu_nodes }} Milan NVIDIA GPU    | aa100          | x86_64 AMD Milan | 1       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA A100 | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       |
| {{ alpine_amc_total_l40_gpu_nodes }} Milan NVIDIA GPU    | al40           | x86_64 AMD Milan | 2       | 64            | 1            |  {{ alpine_standard_ram_per_core }}           | NVIDIA L40  | 3         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 

:::

## Colorado State University contribution

:::{table}
:width: 95%
:widths: auto
:align: left

| Count & Type          | Partition | Processor        | Sockets | Cores (total) | Threads per Core | RAM per Core (GB) | GPU type    | GPU count | Local Disk Capacity & Type | Fabric                                       |
| --------------------- | ------------------- | ---------------- | :-------: | :-------------: | :------------: | :-------------: | ----------- | :---------: | -------------------------- | -------------------------------------------- |
| {{ alpine_csu_total_48_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 2       | 48            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | HDR-100 InfiniBand (200Gb inter-node fabric) |
| {{ alpine_csu_total_32_core_256GB_cpu_nodes }} Milan General CPU  | amilan         | x86_64 AMD Milan | 2       | 32            | 1            |  {{ alpine_standard_ram_per_core }}           | N/A         | 0         | 416G SSD                   | 2x25 Gb Ethernet +RoCE                       | 
:::

