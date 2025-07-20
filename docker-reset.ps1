# reset-docker.ps1

Write-Host "🚨 Iniciando limpeza COMPLETA do Docker..." -ForegroundColor Red

# Parar todos os containers em execução
$containers = docker ps -q
if ($containers) {
    Write-Host "Parando todos os containers em execução..."
    docker stop $containers | Out-Null
}

# Remover todos os containers
$allContainers = docker ps -aq
if ($allContainers) {
    Write-Host "Removendo todos os containers..."
    docker rm -f $allContainers | Out-Null
}

# Remover todas as imagens
$images = docker images -q
if ($images) {
    Write-Host "Removendo todas as imagens..."
    docker rmi -f $images | Out-Null
}

# Remover todos os volumes
$volumes = docker volume ls -q
if ($volumes) {
    Write-Host "Removendo todos os volumes..."
    docker volume rm -f $volumes | Out-Null
}

# Remover redes customizadas (exceto bridge, host e none)
$networks = docker network ls | Select-String -NotMatch "bridge|host|none" | ForEach-Object { ($_ -split '\s+')[0] }
if ($networks) {
    Write-Host "Removendo redes customizadas..."
    foreach ($net in $networks) {
        docker network rm $net | Out-Null
    }
}

# Remover cache de build
Write-Host "Removendo cache de build..."
docker builder prune -a --force | Out-Null

# Executar system prune final para garantir remoção total
Write-Host "Executando docker system prune final..."
docker system prune -a --volumes --force | Out-Null

Write-Host "`n✅ Docker totalmente limpo." -ForegroundColor Green
