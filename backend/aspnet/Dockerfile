#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0.1-bullseye-slim-amd64 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:6.0.101-bullseye-slim-amd64 AS build
WORKDIR /src
COPY ["./FoodinBackend.csproj", "./"]
RUN dotnet restore "./FoodinBackend.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "FoodinBackend.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FoodinBackend.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FoodinBackend.dll"]