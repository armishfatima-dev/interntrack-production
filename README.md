# Interntrack Backend - Week 5: Capstone Production Release

## Overview

This repository contains the complete production-ready backend for InternTrack. It features complete OpenAPI documentation, eager loading query optimizations, local containerization via Docker Compose, and cloud deployment setup.

## Features

- **OpenAPI Documentation:** Interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) with custom descriptions, parameters, and metadata.
- **Optimized Performance:** Solved $N+1$ relationship query overhead using SQLAlchemy `joinedload`.
- **System Health Monitoring:** `/health` endpoint providing live server and PostgreSQL database status.
- **Dockerized Environment:** Automated container setup using Docker and `docker-compose`.

## Running Locally via Docker

```bash
docker-compose up --build

```
